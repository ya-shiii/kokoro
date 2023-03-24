function initFreshChat() {
    window.fcWidget.init({
      token: "715bace3-61b7-421b-929f-96ffa59222e4",
      host: "https://wchat.freshchat.com"
    });
    // Copy the below lines under window.fcWidget.init inside initFreshChat function in the above snippet

  }
  function initialize(i,t){var e;i.getElementById(t)?initFreshChat():((e=i.createElement("script")).id=t,e.async=!0,e.src="https://wchat.freshchat.com/js/widget.js",e.onload=initFreshChat,i.head.appendChild(e))}function initiateCall(){initialize(document,"Freshdesk Messaging-js-sdk")}window.addEventListener?window.addEventListener("load",initiateCall,!1):window.attachEvent("load",initiateCall,!1);