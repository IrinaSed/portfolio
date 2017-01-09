var SYNC_TIME = Date.now() - 10000;
var csrftoken = getCookie('csrftoken');


function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}


function onLoad1() {
    setInterval(sync, 2000);
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
            SYNC_TIME = Date.now();
        },

        error : function () {
            console.log('Ошибка');
        }
    });
}

function sync() {
    $.ajax({
        url: "sync_comments?sync_time=" + SYNC_TIME,
        type: "GET",
        cache: false,

        success : function(json) {
            json.new.forEach(function (element) {
                appendComment(element);
            });
        },

        error : function() {
            console.log('Ошибка');
        }
    });

    SYNC_TIME = Date.now();
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
