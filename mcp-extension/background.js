let pythonPort = null;

// Connect to the native application
function connectToNativeHost() {
  pythonPort = chrome.runtime.connectNative('com.example.python_app');

  pythonPort.onMessage.addListener(function (msg) {
    console.log("Received from Python: ", msg);
  });

  pythonPort.onDisconnect.addListener(function () {
    console.log("Disconnected from Python");
    pythonPort = null;
  });
}

// Listener for messages from popup
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === "runPython") {
    if (!pythonPort) {
      connectToNativeHost();
    }

    pythonPort.postMessage({ command: "execute" });

    setTimeout(() => {
      sendResponse({ result: "Python script executed (sample response)" });
    }, 500);

    return true;
  }
});