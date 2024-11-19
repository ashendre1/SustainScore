chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "sendData") {
    fetch("http://localhost:5000/data", {
      method: "POST",
      headers: {
        "Content-Type": "text/plain"
      },
      body: JSON.stringify(message.data)
    })
    .then(response => {
      base = response.json();
      console.log('response: ', base);
      return base;
    }) 
    .then(data => {
      console.log('data: ', data)
      sendResponse({ data: data })
    })
    .catch(error => {
      console.log('error: ', error);
      sendResponse({ error: error.message })
    });
    return true;
  }
});