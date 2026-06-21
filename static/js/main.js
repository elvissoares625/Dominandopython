// Auto-remove flash messages após 4 segundos
document.addEventListener("DOMContentLoaded", () => {
  const msgs = document.querySelectorAll(".message");
  msgs.forEach(m => {
    setTimeout(() => m.style.opacity = "0", 4000);
    setTimeout(() => m.remove(), 4400);
  });
});
