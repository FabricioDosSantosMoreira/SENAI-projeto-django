// Função para ativar a Sidebar
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar')
  sidebar.classList.toggle('open');
}


// Função para ativar as ações do usuário
function toggleUserActions() {
  const actions = document.getElementById('user-actions')
  actions.classList.toggle('open');
}


// Função para modificar a foto do usuário e já exibir 
function UploadAndChangeUserPhoto() {
  const [file] = event.target.files;
    
  if (file) {
    const imagePreview = document.getElementById('current-image');
    imagePreview.src = URL.createObjectURL(file); // Atualiza a pré-visualização
    imagePreview.style.display = 'block'; // Exibe a imagem caso estivesse oculta
  }
}


// Função para ativar os itens do sidebar
function toggleSidebarInteractiveItem(button, itemId) {

  // Obtém o item interativo correspondente pelo ID
  const interactiveItem = document.getElementById(`interactive-item-for-id-${itemId}`);

  // Fecha os itens não ativos
  document.querySelectorAll('.sidebar-interactive-item').forEach(item => {
    if (item == interactiveItem) {
      item.classList.toggle('open');
    } else {
      item.classList.remove('open');
    }
  });

  // Aqui a altura é corretamente registrada após a animação
  const itemHeight = interactiveItem.clientHeight;

  // Ajuste o marginBottom do botão ativo
  document.querySelectorAll('.sidebar-interactive-button').forEach(btn => {
    if (btn === button && interactiveItem.classList.contains('open')) {
      btn.style.marginBottom = `${itemHeight}px`;
      btn.innerText = btn.innerText.replace("►", "▼");

      // Posiciona o item logo abaixo do botão
      const buttonRect = button.getBoundingClientRect();
      interactiveItem.style.position = 'absolute';
      interactiveItem.style.top = `${buttonRect.bottom}px`;
      interactiveItem.style.left = `${buttonRect.left}px`;

    } else {
      btn.style.marginBottom = '0px';
      btn.innerText = btn.innerText.replace("▼", "►"); 
    }
  });
}


// Gerencia o pop-up de deleção
document.addEventListener('DOMContentLoaded', () => {
  const deleteButtons = document.querySelectorAll('.deleteButton');
  const confirmationPopup = document.getElementById('confirmationPopup');
  const overlay = document.getElementById('overlay');
  const confirmYes = document.getElementById('confirmYes');
  const confirmNo = document.getElementById('confirmNo');
  let deleteUrl = ''; // URL de exclusão temporária

  // Abrir o pop-up de confirmação
  deleteButtons.forEach(button => {
      button.addEventListener('click', (event) => {
          event.preventDefault();
          deleteUrl = button.getAttribute('data-url');
          confirmationPopup.classList.add('show');
          overlay.classList.add('show');
      });
  });

  // Confirmar exclusão
  confirmYes.addEventListener('click', () => {
      window.location.href = deleteUrl;
      confirmationPopup.classList.remove('show');
      overlay.classList.remove('show');
  });

  // Cancelar exclusão
  confirmNo.addEventListener('click', () => {
      confirmationPopup.classList.remove('show');
      overlay.classList.remove('show');
  });
});
