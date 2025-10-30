const btnTopo = document.getElementById("btn-topo");

  // Mostrar/esconder botão
  window.addEventListener("scroll", () => {
    if (window.scrollY > 300) { 
      btnTopo.style.display = "flex";
    } else {
      btnTopo.style.display = "none";
    }
  });

  // Rolagem suave ao clicar
  btnTopo.addEventListener("click", (e) => {
    e.preventDefault(); // evita o salto instantâneo
    document.querySelector('#inicio').scrollIntoView({
      behavior: 'smooth'
    });
  });
