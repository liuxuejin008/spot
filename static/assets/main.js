const shareBtn = document.getElementById('share-btn')

function showToast(message) {
  Toastify({
    text: message || "Copy url Successful!",
    gravity: "top", // `top` or `bottom`
    position: "center", // `left`, `center` or `right`
    style: {
      background: "linear-gradient(to right, #00b09b, #96c93d)",
    },
  }).showToast();
}

shareBtn.addEventListener('click', function () {
  if (navigator.share) {
    navigator.share({
      title: 'AI Travel',
      text: document.getElementById('js-title').innerText || 'Use AI to plan your next trip!',
      url: document.location.href,
    })
      .then(() => console.log('Successful share'))
      .catch((error) => console.log('Error sharing', error));
  } else {
    const input = document.createElement('input');
    input.value = document.location.href;
    document.body.appendChild(input);
    input.select();
    document.execCommand('copy');
    document.body.removeChild(input);

    showToast()

  }
})