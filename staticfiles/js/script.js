// Auto-dismiss alert messages after 3 seconds
document.addEventListener("DOMContentLoaded", function () {
  // Get all alert messages
  const alerts = document.querySelectorAll(".alert");

  alerts.forEach(function (alert) {
    // Auto dismiss after 3 seconds
    setTimeout(function () {
      // Fade out the alert
      alert.style.transition = "opacity 0.5s ease";
      alert.style.opacity = "0";
      setTimeout(function () {
        alert.remove();
      }, 500);
    }, 3000);
  });
});
