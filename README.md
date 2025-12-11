this is my unblocked games google site, migrated to github pages.


















download source zip for less chance of blockings
lol even my teacher is playing the site


about blank formula for fun chat:
<div class="box">
  <button id="openFile">Eaglercraft ABOUT:BLANK</button>
</div>

<script>
document.getElementById("openFile").addEventListener("click", () => {
  // Correct raw URL (no refs/heads)
  const url = "https://raw.githubusercontent.com/JWM7210/site-test/main/eagl.html";

  // Open the new window synchronously so the browser treats it as a user gesture
  const win = window.open("about:blank", "_blank");

  if (!win) {
    alert("Popup blocked. Allow popups for this site and try again.");
    return;
  }

  // Fetch and inject
  fetch(url)
    .then(response => {
      if (!response.ok) throw new Error(response.status + " " + response.statusText);
      return response.text();
    })
    .then(html => {
      // Optional: set a base so relative URLs resolve to your repo's raw root
      const baseHref = "https://raw.githubusercontent.com/JWM7210/site-test/main/";
      const baseTag = `<base href="${baseHref}">`;

      win.document.open();
      win.document.write(baseTag + html);
      win.document.close();
    })
    .catch(err => {
      win.document.open();
      win.document.write(`<pre style="color:red">Error loading file: ${err.message}</pre>`);
      win.document.close();
    });
});
</script>
