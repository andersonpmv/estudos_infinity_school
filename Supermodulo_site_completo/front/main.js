// ================= MENU LATERAL =================
const btn = document.getElementById('menu-btn');
const menu = document.getElementById('menu-lateral');

// Abrir/fechar com clique
btn.addEventListener('click', () => {
  menu.classList.toggle('ativo');
  btn.classList.toggle('ativo');
});

// Abrir menu ao passar o mouse sobre o botão
btn.addEventListener('mouseover', () => {
  menu.classList.add('ativo');
  btn.classList.add('ativo');
});

// Fechar menu quando o mouse sair do menu lateral
menu.addEventListener('mouseleave', () => {
  menu.classList.remove('ativo');
  btn.classList.remove('ativo');
});

// ================= CARROSSEL DE CURSOS =================
const carousel = document.querySelector('.cursos_in');
const prevBtn = document.querySelector('.carousel-btn.prev');
const nextBtn = document.querySelector('.carousel-btn.next');
const wrapper = document.querySelector('.carousel-wrapper');
const scrollAmount = 340; // quanto anda a cada clique
let autoScroll;
let direction = 1; // 1 = direita, -1 = esquerda

function scrollParaMultiversos() {
  document.getElementById("sobre_multiverso").scrollIntoView({ behavior: "smooth" });
}

// Botões manuais
nextBtn.addEventListener('click', () => {
  carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
});
prevBtn.addEventListener('click', () => {
  carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
});

// Auto-scroll
function startAutoScroll() {
  autoScroll = setInterval(() => {
    const maxScroll = carousel.scrollWidth - carousel.clientWidth;

    if (carousel.scrollLeft >= maxScroll - 5) direction = -1;
    if (carousel.scrollLeft <= 0) direction = 1;

    carousel.scrollBy({ left: direction * 2, behavior: 'smooth' });
  }, 30);
}

function stopAutoScroll() {
  clearInterval(autoScroll);
}

startAutoScroll();
wrapper.addEventListener('mouseenter', stopAutoScroll);
wrapper.addEventListener('mouseleave', startAutoScroll);

// ================= MULTIVERSOS (descrição dinâmica) =================
const botoes = document.querySelectorAll(".btn");
const descricao = document.getElementById("descricao");

botoes.forEach(btn => {
  btn.addEventListener("mouseenter", () => {
    descricao.textContent = btn.getAttribute("data-text");
    descricao.style.color = "#ff0040";
  });

  btn.addEventListener("mouseleave", () => {
    descricao.textContent = "Passe o mouse sobre um nível para descobrir o que o espera.";
    descricao.style.color = "#ccc";
  });
});

// ================= CARROSSEL DE RANKING =================
const track = document.querySelector(".carousel-track");
const btnPrev = document.querySelector(".carousel-btn.prev");
const btnNext = document.querySelector(".carousel-btn.next");

btnNext.addEventListener("click", () => {
  track.scrollBy({ left: 300, behavior: "smooth" });
});
btnPrev.addEventListener("click", () => {
  track.scrollBy({ left: -300, behavior: "smooth" });
});
