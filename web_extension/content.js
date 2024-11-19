chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "scrapeData") {
    const scrapedData = document.body.innerText; // Example: scrape the entire text of the page
    sendResponse({ data: scrapedData });
  }
});