document.getElementById("scrapeButton").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "scrapeData" }, (response) => {
      if (response && response.data) {
        chrome.runtime.sendMessage({ action: "sendData", data: response.data }, (response) => {
          console.log('yellow: ', response);
          if (response && response.data) {
            document.getElementById('scoreField').innerText = response.data.data +'/10';
          } else {
            document.getElementById('scoreField').innerText = 'Error: ' + response.error;
          }
        });
      }
    });
  });
});