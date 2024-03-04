function execute(){ 
    const agent = window.navigator.userAgent.toLowerCase();
    let browserName;
    let browserImage;
    switch (true) {
        case agent.indexOf("edge") > -1:
            browserName = "MS Edge";
            browserImage = new Image();
            browserImage.src = "https://play-lh.googleusercontent.com/VYvJqGnrQiKkbbyLyMeiL-GM3go4tBIA64uVEGQazLXD4p_M3F45kHyt42o_6d5VXA"
            break;
        case agent.indexOf("edg/") > -1:
            browserName = "Edge (chromium based)";
            browserImage = new Image();
            browserImage.src = "https://play-lh.googleusercontent.com/VYvJqGnrQiKkbbyLyMeiL-GM3go4tBIA64uVEGQazLXD4p_M3F45kHyt42o_6d5VXA"
            break;
        case agent.indexOf("opr") > -1 && !!window.opr:
            browserName = "Opera";
            browserImage = new Image();
            browserImage.src = "data:image/jpeg;base64,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"
            break;
        case agent.indexOf("chrome") > -1 && !!window.chrome:
            browserName = "Chrome";
            browserImage = new Image();
            browserImage.src = "data:image/jpeg;base64,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"
            break;
        case agent.indexOf("trident") > -1:
            browserName = "MS IE";
            browserImage = new Image();
            browserImage.src = "https://w7.pngwing.com/pngs/1007/876/png-transparent-internet-explorer-9-web-browser-computer-icons-internet-explorer-blue-text-window-thumbnail.png"
            break;
        case agent.indexOf("firefox") > -1:
            browserName = "Mozilla Firefox";
            browserImage = new Image();
            browserImage.src = "https://cdn0.iconfinder.com/data/icons/mozilla-icons/256/firefox_png.png"
            break;
        case agent.indexOf("safari") > -1:
            browserName = "Safari";
            browserImage = new Image();
            browserImage.src = "https://1000logos.net/wp-content/uploads/2020/08/Safari-Logo.png"
            break;
        default:
            browserName = "other";
            browserImage = new Image();
            browserImage.src = "https://images.twinkl.co.uk/tw1n/image/private/t_630/u/ux/question-mark_ver_1.jpg"
    }
    document.querySelector("h1").innerText = browserName;
    console.log(browserName);
    document.querySelector("p").appendChild(browserImage);
}