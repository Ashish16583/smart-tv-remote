const cacheName = "tv-remote-cache-v1";
const assetsToCache = [
  "/",
  "/manifest.json",
  "/static/icon.png",
  "/static/youtube.png",
  "/static/netflix.png",
  "/static/prime.png",
  "/static/hotstar.png"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(cacheName).then(cache => {
      return cache.addAll(assetsToCache);
    })
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(resp => {
      return resp || fetch(event.request);
    })
  );
});
