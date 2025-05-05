document.getElementById('runPython').addEventListener('click', function () {
  chrome.runtime.sendMessage({ action: "runPython" }, function (response) {
    document.getElementById('output').textContent = response.result;
  });
});