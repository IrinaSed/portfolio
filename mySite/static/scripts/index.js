function onEsc(event) {
    orderPhoto = ['#ekb', '#bonfire', '#hightEkb', '#mat-mex', '#konfuzy', '#karacul'];
    if (event.which == 27) {
        location.hash = '#';
    }
    var indPhoto = orderPhoto.indexOf(location.hash);
    if (event.which == 39 && indPhoto !== -1) {
        if (orderPhoto.length > indPhoto + 1) {
            location.hash = orderPhoto[indPhoto + 1];
        } else {
            location.hash = orderPhoto[0];
        }
    } else if (event.which == 37 && indPhoto !== -1) {
        if (indPhoto - 1 >= 0) {
            location.hash = orderPhoto[indPhoto - 1];
        } else {
            location.hash = orderPhoto[orderPhoto.length - 1];
        }
    }

}

function avoidInvalidKeyStorkes(evtArg) {
    var evt = (document.all ? window.event : evtArg);
    var isIE = (document.all ? true : false);
    var KEYCODE = (document.all ? window.event.keyCode : evtArg.which);

    var element = (document.all ? window.event.srcElement : evtArg.target);

    if (KEYCODE == "112") {
        if (isIE) {
            document.onhelp = function() {
                return (false);
            };
            window.onhelp = function() {
                return (false);
            };
        }
        evt.returnValue = false;
        evt.keyCode = 0;
        evt.preventDefault();
        evt.stopPropagation();
        location.hash = '#help'
    }

    window.status = "Done";
}

function onLoad() {
    if (window.document.addEventListener) {
    window.document.addEventListener("keydown", avoidInvalidKeyStorkes, false);
    } else {
        window.document.attachEvent("onkeydown", avoidInvalidKeyStorkes);
        document.captureEvents(Event.KEYDOWN);
    }
}
