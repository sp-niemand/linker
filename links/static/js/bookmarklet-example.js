(function () {
    var screenWidth = screen.width,
        screenHeight = screen.height,
        popupWidth = 640,
        popupHeight = 580,
        popupLeft = 0,
        popupTop = 0;
    if (screenWidth > popupWidth) {
        popupLeft = Math.round((screenWidth / 2) - (popupWidth / 2));
    }
    if (screenHeight > popupHeight) {
        popupTop = Math.round((screenHeight / 2) - (popupHeight / 2));
    }
    window.open('https://wiki.murka.com/plugins/sharelinksbookmarklet/bookmarklet.action?bookmarkedURL=' + encodeURIComponent(window.location.href), '', 'left=' +
    popupLeft + ',top=' + popupTop + ',width=' + popupWidth + ',height=' + popupHeight + ',personalbar=0,toolbar=0,scrollbars=1,resizable=1');
}());
