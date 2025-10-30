let editProjectCard = null;

// ================== Alternar seções ==================
const menuItems = document.querySelectorAll('.menu-item');
const sections = document.querySelectorAll('.content-section');

menuItems.forEach(item => {
  item.addEventListener('click', () => {
    menuItems.forEach(i => i.classList.remove('active'));
    item.classList.add('active');

    const sectionId = item.dataset.section;
    sections.forEach(sec => sec.style.display = 'none');
    document.getElementById(sectionId).style.display = 'block';
  });
});

// ================== Mostrar nome do arquivo selecionado ==================
const arquivoInput = document.getElementById('arquivoProjeto');
const nomeArquivoSpan = document.getElementById('nomeArquivo');

arquivoInput.addEventListener('change', () => {
  const fileName = arquivoInput.files.length > 0 ? arquivoInput.files[0].name : "Nenhum arquivo escolhido";
  nomeArquivoSpan.textContent = fileName;
});

// ================== Lista de projetos ==================
const listaProjetos = document.getElementById('listaProjetos');

function atualizarMensagemProjetos() {
  if(listaProjetos.children.length === 0) {
    listaProjetos.innerHTML = `<p style="color:#999; font-style:italic;">Nenhum projeto cadastrado</p>`;
  } else {
    const primeiraFilha = listaProjetos.children[0];
    if(primeiraFilha.tagName === 'P' && primeiraFilha.textContent.includes('Nenhum projeto cadastrado')) {
      primeiraFilha.remove();
    }
  }
}
atualizarMensagemProjetos();

// ================== Adicionar ou editar projeto ==================
const formProjeto = document.getElementById('formProjeto');

formProjeto.addEventListener('submit', (e) => {
  e.preventDefault();
  const nome = document.getElementById('nomeProjeto').value;
  const categoria = document.getElementById('categoriaProjeto').value;
  const descricao = document.getElementById('descricaoProjeto').value;
  const arquivo = arquivoInput.files.length > 0 ? arquivoInput.files[0].name : "Nenhum arquivo";

  if(editProjectCard){
    editProjectCard.querySelector('h4').textContent = nome;
    editProjectCard.querySelector('.categoria').textContent = `Categoria: ${categoria}`;
    editProjectCard.querySelector('.descricao').textContent = descricao;
    editProjectCard.querySelector('.arquivo').textContent = `Arquivo: ${arquivo}`;
    editProjectCard = null;
    document.getElementById('formTitle').textContent = "Criar Novo Projeto";
  } else {
    const card = document.createElement('div');
    card.classList.add('projeto-card');
    card.innerHTML = `
      <h4>${nome}</h4>
      <p class="categoria">Categoria: ${categoria}</p>
      <p class="descricao">${descricao}</p>
      <p class="arquivo">Arquivo: ${arquivo}</p>
      <div class="projeto-botoes">
        <button class="btn-editar">Editar</button>
        <button class="btn-deletar">Deletar</button>
      </div>
    `;
    listaProjetos.appendChild(card);
  }

  formProjeto.reset();
  nomeArquivoSpan.textContent = "Nenhum arquivo escolhido";
  atualizarMensagemProjetos();
});

// ================== Delegação de eventos para editar e deletar ==================
listaProjetos.addEventListener('click', (e) => {
  const card = e.target.closest('.projeto-card');
  if(!card) return;

  if(e.target.classList.contains('btn-editar')){
    editProjectCard = card;
    document.getElementById('nomeProjeto').value = card.querySelector('h4').textContent;
    document.getElementById('categoriaProjeto').value = card.querySelector('.categoria').textContent.split(': ')[1];
    document.getElementById('descricaoProjeto').value = card.querySelector('.descricao').textContent;
    document.getElementById('formTitle').textContent = "Editar Projeto";
    card.scrollIntoView({behavior: "smooth", block: "start"});
  }

  if(e.target.classList.contains('btn-deletar')){
    const confirmModal = document.getElementById('confirmModal');
    confirmModal.style.display = 'flex';
    document.getElementById('confirmText').textContent = `Tem certeza que deseja deletar o projeto "${card.querySelector('h4').textContent}"?`;

    document.getElementById('btnSim').onclick = () => { 
      card.remove(); 
      confirmModal.style.display = 'none';
      atualizarMensagemProjetos();
    };
    document.getElementById('btnNao').onclick = () => { confirmModal.style.display = 'none'; };
  }
});

// ================== Gráficos Dashboard ==================
function criarGrafico(ctxEl, type, labels, data, options = {}) {
  if(!ctxEl) return;
  const ctx = ctxEl.getContext('2d');
  return new Chart(ctx, { type, data, options });
}

const ctxSemanal = document.getElementById('graficoSemanal');
criarGrafico(ctxSemanal, 'bar', ['Seg','Ter','Qua','Qui','Sex','Sáb','Dom'], [12,19,14,20,18,25,22], { responsive:true, plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true}} });

const ctxMensal = document.getElementById('graficoMensal');
criarGrafico(ctxMensal, 'line', ['Jan','Fev','Mar','Abr','Mai','Jun'], [75,80,85,70,90,95], { responsive:true, plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true, max:100}} });

// ================== DISCÍPULOS ==================
const inputBusca = document.getElementById('inputBuscaDiscipulo');
const btnBuscar = document.getElementById('btnBuscarDiscipulo');
const listaResultados = document.getElementById('resultadosDiscipulos');
const containerResultados = document.getElementById('listaResultados');
const resultadoDiscipulo = document.getElementById('resultadoDiscipulo');
const formEditarDiscipulo = document.getElementById('formEditarDiscipulo');

// Dados simulados
const todosDiscipulos = [
  { id: 1, nome: "Ailton Daniel", curso: "Programação Full Stack", projetos: 15, resolvidos: 12, foto: "images/user-placeholder.png", telefone:"123456789", email:"ailton@email.com" },
  { id: 2, nome: "Ailton dos Santos", curso: "Design UI/UX", projetos: 8, resolvidos: 5, foto: "images/user-placeholder.png", telefone:"987654321", email:"ailton2@email.com" },
  { id: 3, nome: "Daniele Silva", curso: "Marketing Digital", projetos: 10, resolvidos: 7, foto: "images/user-placeholder.png", telefone:"111222333", email:"daniele@email.com" },
  { id: 4, nome: "Daniel Souza", curso: "Fotografia", projetos: 6, resolvidos: 3, foto: "images/user-placeholder.png", telefone:"444555666", email:"daniel@email.com" }
];

// Função buscar discípulo
async function buscarDiscipulo() {
  const nome = inputBusca.value.trim().toLowerCase();
  if(nome === "") { alert("Digite o nome do discípulo."); return; }

  const encontrados = todosDiscipulos.filter(d => d.nome.toLowerCase().includes(nome));
  listaResultados.innerHTML = '';
  containerResultados.style.display = encontrados.length ? 'block' : 'none';
  resultadoDiscipulo.style.display = 'none';
  formEditarDiscipulo.style.display = 'none';

  if(encontrados.length === 0) { alert("Nenhum discípulo encontrado."); return; }

  encontrados.forEach(d => {
    const item = document.createElement('div');
    item.className = "item-discipulo";
    item.innerHTML = `<img src="${d.foto}" alt="${d.nome}"><span>${d.nome}</span>`;
    item.onclick = () => mostrarDetalhesDiscipulo(d);
    listaResultados.appendChild(item);
  });
}

// Permite apertar Enter
inputBusca.addEventListener('keydown', (e)=>{ if(e.key==='Enter'){ e.preventDefault(); buscarDiscipulo(); } });
btnBuscar.addEventListener('click', buscarDiscipulo);

// Função mostrar detalhes
let graficoDiscipulo = null;
function mostrarDetalhesDiscipulo(d) {
  containerResultados.style.display = 'none';
  resultadoDiscipulo.style.display = 'flex';
  resultadoDiscipulo.querySelector('#fotoDiscipulo').src = d.foto;
  resultadoDiscipulo.querySelector('#nomeDiscipulo').textContent = d.nome;
  resultadoDiscipulo.querySelector('#cursoDiscipulo').textContent = `Curso: ${d.curso}`;
  resultadoDiscipulo.querySelector('#projetosDiscipulo').textContent = `Projetos: ${d.projetos}`;

  const porcentagem = ((d.resolvidos/d.projetos)*100).toFixed(1);
  document.getElementById('textoPorcentagem').textContent = `Projetos concluídos: ${d.resolvidos}/${d.projetos} (${porcentagem}%)`;

  const ctx = document.getElementById('graficoProjetosDiscipulo').getContext('2d');
  if(graficoDiscipulo) graficoDiscipulo.destroy();
  graficoDiscipulo = new Chart(ctx, {
    type:'doughnut',
    data:{ labels:['Concluídos','Pendentes'], datasets:[{ data:[d.resolvidos, d.projetos-d.resolvidos], backgroundColor:['#00ff95','#444'], borderWidth:0 }] },
    options:{ responsive:true, plugins:{legend:{position:'top', labels:{color:'#fff'}}} }
  });

  // Botões Editar / Deletar
  resultadoDiscipulo.querySelector('.btn-editar-dados').onclick = () => {
    formEditarDiscipulo.style.display = 'block';
    formEditarDiscipulo.querySelector('#editarNome').value = d.nome;
    formEditarDiscipulo.querySelector('#editarCurso').value = d.curso;
    formEditarDiscipulo.querySelector('#editarTelefone').value = d.telefone || '';
    formEditarDiscipulo.querySelector('#editarEmail').value = d.email || '';
  };
  resultadoDiscipulo.querySelector('.btn-deletar-discipulo').onclick = () => {
    if(confirm(`Deseja deletar o discípulo ${d.nome}?`)) {
      todosDiscipulos.splice(todosDiscipulos.indexOf(d),1);
      resultadoDiscipulo.style.display = 'none';
      formEditarDiscipulo.style.display = 'none';
      alert("Discípulo deletado com sucesso.");
    }
  };
}

// Salvar alterações do discípulo
formEditarDiscipulo.addEventListener('submit', (e)=>{
  e.preventDefault();
  const nome = formEditarDiscipulo.querySelector('#editarNome').value;
  const curso = formEditarDiscipulo.querySelector('#editarCurso').value;
  const telefone = formEditarDiscipulo.querySelector('#editarTelefone').value;
  const email = formEditarDiscipulo.querySelector('#editarEmail').value;

  // Atualiza dados do discípulo (simulado)
  const nomeOriginal = document.getElementById('nomeDiscipulo').textContent;
  const d = todosDiscipulos.find(d => d.nome === nomeOriginal);
  if(d){
    d.nome = nome;
    d.curso = curso;
    d.telefone = telefone;
    d.email = email;
    mostrarDetalhesDiscipulo(d);
    formEditarDiscipulo.style.display = 'none';
    alert("Dados atualizados com sucesso.");
  }
});
