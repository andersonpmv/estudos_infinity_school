// ===== DADOS SIMULADOS =====
const aluno = {
  nome: "João Silva",
  foto: "https://i.pravatar.cc/32?img=10",
  cadastroConcluido: true,
  nivelAtual:"iniciante",
  projetos: {
    iniciante:[{titulo:"Projeto A", descricao:"Descrição do projeto A"},{titulo:"Projeto B", descricao:"Descrição do projeto B"}],
    intermediario:[{titulo:"Projeto C", descricao:"Descrição do projeto C"}],
    avancado:[{titulo:"Projeto D", descricao:"Descrição do projeto D"}]
  },
  meusProjetos:[]
};

let projetoSelecionado = null;

// ===== BOTÃO DISCÍPULO =====
function atualizarBotaoDiscipulo(){
  const btn = document.getElementById("botao-discipulo");
  btn.innerHTML="";
  const img = document.createElement("img");
  img.src = aluno.foto;
  img.alt = aluno.nome;
  const span = document.createElement("span");
  span.textContent = aluno.nome;
  btn.appendChild(img);
  btn.appendChild(span);
}

// ===== RENDERIZAÇÃO DE NÍVEL =====
function renderNivel(nivel){
  document.querySelectorAll(".nivel-section").forEach(sec=>sec.style.display="none");
  document.getElementById(`${nivel}-section`).style.display="block";

  const container = document.getElementById(`projetos-${nivel}`);
  container.innerHTML="";
  aluno.projetos[nivel].forEach(proj=>{
    const card = document.createElement("div");
    card.classList.add("card");
    card.innerHTML=`<h4>${proj.titulo}</h4><p>${proj.descricao}</p>
      <button onclick="participarProjeto('${nivel}','${proj.titulo}')">Participar</button>`;
    container.appendChild(card);
  });
}

// ===== PARTICIPAR PROJETO =====
function participarProjeto(nivel,titulo){
  const projetoIndex = aluno.projetos[nivel].findIndex(p=>p.titulo===titulo);
  if(projetoIndex!==-1){
    const projeto = aluno.projetos[nivel].splice(projetoIndex,1)[0];
    aluno.meusProjetos.unshift({...projeto, status:"andamento"}); // adiciona no topo
    renderNivel(nivel); // mantém na tela do nível
  }
}

// ===== ATUALIZAR MEUS PROJETOS =====
function atualizarMeusProjetos(){
  document.querySelectorAll(".nivel-section").forEach(sec=>sec.style.display="none");
  document.getElementById("meus-projetos-section").style.display="block";

  // Contadores
  const andamento = aluno.meusProjetos.filter(p=>p.status==="andamento").length;
  const concluidos = aluno.meusProjetos.filter(p=>p.status==="concluido").length;
  document.getElementById("qtd-andamento").textContent=andamento;
  document.getElementById("qtd-concluidos").textContent=concluidos;
  document.getElementById("qtd-disponiveis").textContent = aluno.projetos[aluno.nivelAtual].length;

  // Projetos do aluno
  const container = document.getElementById("projetos-meus");
  container.innerHTML="";
  aluno.meusProjetos.forEach(proj=>{
    const card = document.createElement("div");
    card.classList.add("card");
    card.innerHTML=`<h4>${proj.titulo}</h4><p>${proj.descricao}</p>
      <button onclick="abrirModal('${proj.titulo}')">Entregar</button>`;
    container.appendChild(card);
  });

  // Ranking fake
  const rankingContainer = document.getElementById("ranking-container");
  rankingContainer.innerHTML="";
  const lista = document.createElement("div");
  lista.classList.add("ranking-list");
  for(let i=1;i<=5;i++){
    const item = document.createElement("div");
    item.classList.add("ranking-item");
    item.innerHTML=`<span>${i}º</span><img src="https://i.pravatar.cc/40?img=${i}" alt="Aluno ${i}"><span>Aluno ${i}</span>`;
    lista.appendChild(item);
  }
  rankingContainer.appendChild(lista);
}

// ===== MODAL DE ENTREGA =====
function abrirModal(titulo){
  projetoSelecionado = titulo;
  document.getElementById("modal-entrega").style.display="flex";
}
document.getElementById("fechar-modal").addEventListener("click",()=>{
  document.getElementById("modal-entrega").style.display="none";
});
document.getElementById("confirmar-entrega").addEventListener("click",()=>{
  const tipo = document.querySelector('.modal-content button[data-tipo].active')?.dataset.tipo || 'arquivo';
  const link = document.getElementById("link-entrega").value;
  const proj = aluno.meusProjetos.find(p=>p.titulo===projetoSelecionado);
  if(proj){ proj.status="concluido"; proj.entrega={tipo,link}; }
  document.getElementById("modal-entrega").style.display="none";
  atualizarMeusProjetos();
});
document.querySelectorAll(".modal-content button[data-tipo]").forEach(btn=>{
  btn.addEventListener("click",()=>{
    document.querySelectorAll(".modal-content button[data-tipo]").forEach(b=>b.classList.remove("active"));
    btn.classList.add("active");
  });
});

// ===== SIDEBAR =====
document.querySelectorAll(".nivel-btn").forEach(btn=>{
  btn.addEventListener("click",()=>{
    if(btn.classList.contains("active")) return;
    document.querySelectorAll(".nivel-btn, .meus-projetos-btn").forEach(b=>b.classList.remove("active"));
    btn.classList.add("active");

    // Esconde "Meus Projetos" ao voltar para nível
    document.getElementById("meus-projetos-section").style.display = "none";
    renderNivel(btn.dataset.nivel);
  });
});
document.querySelector(".meus-projetos-btn").addEventListener("click",()=>{
  document.querySelectorAll(".nivel-btn, .meus-projetos-btn").forEach(b=>b.classList.remove("active"));
  document.querySelector(".meus-projetos-btn").classList.add("active");
  atualizarMeusProjetos();
});

// ===== INIT =====
document.addEventListener("DOMContentLoaded",()=>{
  atualizarBotaoDiscipulo();
  renderNivel(aluno.nivelAtual);
});
