function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}


function onLoad1() {
    $('.comment-form').on('submit', function (event) {
        event.preventDefault();
        comment();
    });
}


function appendComment(json) {
    $('.common-comments').append(
        '<div class="comment">'
        + '<div class="comment-message">'
        + '<pre>' + json.message + '</pre></div>'
        + '<div class="comment-username">'
        + json.username + '</div></div>'
    );
}

function comment() {
    $.ajax({
        url: "comment",
        type: "POST",
        cache: false,
        dataType: "json",
        data : {
            message: $('#message').val(),
            username: $('#username').val()
        },

        success : function(json) {
            $('#message').val('');
            $('#username').val('');
            appendComment(json);
        },

        error : function () {
            console.log('Ошибка');
        }
    });
}

function like(anchor) {
    $.ajax({
        url: "like?anchor=" + anchor,
        type: "GET",
        cache: false,

        success : function(json) {
            $('.likes-count').each(function () {
                var _this = $(this);
                _this.attr('src', _this.attr('src') + '&rnd=' + Math.random());
            });
        },

        error : function () {
            console.log('Ошибка');
        }
    });
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
