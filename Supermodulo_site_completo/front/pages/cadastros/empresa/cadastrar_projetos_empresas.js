const fileInput = document.getElementById('arquivo');
const fileName = document.querySelector('.file-name');
const fileButton = document.querySelector('.custom-file span:first-child');

fileButton.addEventListener('click', () => {
    fileInput.click(); // Abre o seletor de arquivos
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        fileName.textContent = fileInput.files[0].name;
    } else {
        fileName.textContent = "Nenhum arquivo selecionado";
    }
});
