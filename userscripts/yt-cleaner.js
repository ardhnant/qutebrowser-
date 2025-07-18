#!/usr/bin/env qutebrowser-userscript
(() => {
  const removeYouTubeAds = () => {
    // Remove promoted/sponsored videos
    document.querySelectorAll("ytd-video-renderer,ytd-grid-video-renderer,ytd-rich-item-renderer").forEach(el => {
      if (el.innerText.toLowerCase().includes("ad ·") || el.innerText.toLowerCase().includes("sponsored")) {
        el.remove();
      }
    });

    // Remove Shorts (optional)
    document.querySelectorAll("ytd-rich-section-renderer").forEach(el => {
      if (el.innerText.toLowerCase().includes("shorts")) {
        el.remove();
      }
    });
  };

  removeYouTubeAds();

  // Keep cleaning when new content loads
  new MutationObserver(removeYouTubeAds).observe(document.body, {
    childList: true,
    subtree: true
  });
})();
