import { supabase } from '../../../supabaseClient.js';

/* ======================================================
   1️⃣ Carregar lista de cursos do Supabase no <select>
====================================================== */
async function carregarCursos() {
  const { data, error } = await supabase.from('cursos').select('id, nome');
  const select = document.getElementById('curso');

  if (error) {
    console.error("Erro ao carregar cursos:", error.message);
    return;
  }

  data.forEach(curso => {
    const opt = document.createElement('option');
    opt.value = curso.nome; // ou curso.id se preferir vincular via FK
    opt.textContent = curso.nome;
    select.appendChild(opt);
  });
}

// Executa a função ao carregar a página
carregarCursos();


// ===============================
// Função auxiliar de mensagens
// ===============================
function exibirMensagem(texto, tipo = 'erro') {
  const msg = document.getElementById('mensagem');
  msg.textContent = texto;
  msg.style.color = tipo === 'erro' ? 'red' : 'limegreen';
  msg.style.fontWeight = 'bold';
  msg.style.marginTop = '10px';
  msg.style.textAlign = 'center';
}

// ===============================
// Máscara CPF e Telefone
// ===============================
document.getElementById('cpf').addEventListener('input', (e) => {
  let v = e.target.value.replace(/\D/g, '');
  v = v.replace(/(\d{3})(\d)/, '$1.$2');
  v = v.replace(/(\d{3})(\d)/, '$1.$2');
  v = v.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
  e.target.value = v;
});

document.getElementById('telefone').addEventListener('input', (e) => {
  let v = e.target.value.replace(/\D/g, '');
  v = v.replace(/^(\d{2})(\d)/g, '($1) $2');
  v = v.replace(/(\d{5})(\d{4})$/, '$1-$2');
  e.target.value = v;
});

// ===============================
// Preview da foto
// ===============================
const fotoInput = document.getElementById('foto');
const preview = document.getElementById('previewFoto');

fotoInput.addEventListener('change', function () {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      preview.src = e.target.result;
      document.querySelector('.foto-aluno').classList.add('has-photo');
    };
    reader.readAsDataURL(file);
  }
});

// ===============================
// Validações de campos
// ===============================
function validarNome(nome) {
  const regex = /^[A-Za-zÀ-ÿ\s]{3,}$/;
  return regex.test(nome.trim());
}

function validarCPF(cpf) {
  cpf = cpf.replace(/[^\d]+/g, ''); // remove pontos e traços

  if (cpf.length !== 11) return false;

  // elimina CPFs inválidos conhecidos
  if (/^(\d)\1{10}$/.test(cpf)) return false;

  let soma = 0;
  let resto;

  // primeiro dígito verificador
  for (let i = 1; i <= 9; i++) soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
  resto = (soma * 10) % 11;
  if (resto === 10 || resto === 11) resto = 0;
  if (resto !== parseInt(cpf.substring(9, 10))) return false;

  soma = 0;

  // segundo dígito verificador
  for (let i = 1; i <= 10; i++) soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
  resto = (soma * 10) % 11;
  if (resto === 10 || resto === 11) resto = 0;
  if (resto !== parseInt(cpf.substring(10, 11))) return false;

  return true;

}

function validarTelefone(telefone) {
  const regex = /^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$/;
  return regex.test(telefone);
}

function validarIdade(dataNascimento) {
  const dataNasc = new Date(dataNascimento);
  const hoje = new Date();
  const idade = hoje.getFullYear() - dataNasc.getFullYear();
  const mes = hoje.getMonth() - dataNasc.getMonth();
  if (mes < 0 || (mes === 0 && hoje.getDate() < dataNasc.getDate())) {
    return idade - 1 >= 10;
  }
  return idade >= 10;
}

// ===============================
// Envio do formulário
// ===============================
document.getElementById('cadastroForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const nome = document.getElementById('nome').value.trim();
  const cpf = document.getElementById('cpf').value.trim();
  const data_nascimento = document.getElementById('dataNascimento').value;
  const curso = document.getElementById('curso').value.trim();
  const telefone = document.getElementById('telefone').value.trim();
  const email = document.getElementById('email').value.trim();
  const foto_url = preview.src !== 'https://via.placeholder.com/120' ? preview.src : null;

  // ========== Validações ==========
  if (!validarNome(nome)) return exibirMensagem('❌ Inválido! Use apenas letras e espaços (mín. 3 caracteres).');
  if (!validarCPF(cpf)) return exibirMensagem('❌ CPF inválido!');
  if (!validarTelefone(telefone)) return exibirMensagem('❌ Inválido. Use o formato (11) 91234-5678.');
  if (!validarIdade(data_nascimento)) return exibirMensagem('❌ Discipulo novo demais. Idade minima 10 anos.');
  if (!curso) return exibirMensagem('❌ Selecione o curso.');
  if (email && !email.includes('@')) return exibirMensagem('❌ E-mail inválido.');

  // ========== Envio (Supabase) ==========
  try {
    const { error } = await supabase
      .from('alunos_autorizados')
      .insert([{ nome, cpf, data_nascimento, telefone, email, curso }]);


    if (error) {
      exibirMensagem('❌ Erro ao cadastrar aluno: ' + error.message);
    } else {
      exibirMensagem('✅ Aluno cadastrado com sucesso!', 'sucesso');
      e.target.reset();
      preview.src = 'https://via.placeholder.com/120';
      document.querySelector('.foto-aluno').classList.remove('has-photo');
    }
  } catch (err) {
    exibirMensagem('⚠️ Erro inesperado: ' + err.message);
  }
});
