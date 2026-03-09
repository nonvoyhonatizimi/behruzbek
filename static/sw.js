const CACHE_NAME = 'nonvoyhona-v5';
const ASSETS = [
  '/',
  '/static/css/apple-style.css',
  '/static/img/logo.png',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      // Just try to cache, don't worry if it fails
      return Promise.allSettled(ASSETS.map(url => 
        fetch(url).then(response => {
           if (response.ok) return cache.put(url, response);
        }).catch(() => {})
      ));
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      );
    })
  );
  return self.clients.claim();
});

// Disabled fetch for now to prevent "No Internet" errors on Safari
// self.addEventListener('fetch', (event) => { ... });
