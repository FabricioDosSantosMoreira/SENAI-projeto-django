// Função para ativar a sidebar
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar')
  sidebar.classList.toggle('open');
}


// Função para ativar as ações do usuário
function toggleUserActions() {
  const actions = document.getElementById('user-actions')
  actions.classList.toggle('open');
}


// Função para modificar a foto do usuário e já exibir no formulário
function UploadAndChangeFormPhoto() {
  const [file] = event.target.files;

  if (file) {
    const imagePreview = document.getElementById('current-image');
    imagePreview.src = URL.createObjectURL(file); // Atualiza a pré-visualização
    imagePreview.style.display = 'block';
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

  // Obtêm a altura do item interativo
  const itemHeight = interactiveItem.clientHeight;

  // Muda o símbolo do botão e posiciona o item interativo corretamente
  document.querySelectorAll('.sidebar-interactive-button').forEach(btn => {
    if (btn === button && interactiveItem.classList.contains('open')) {
      // Muda o símbolo do botão (abre)
      btn.style.marginBottom = `${itemHeight}px`;
      btn.innerText = btn.innerText.replace("►", "▼");

      // Posiciona o item interativo logo abaixo do botão
      const buttonRect = button.getBoundingClientRect();
      interactiveItem.style.position = 'absolute';
      interactiveItem.style.top = `${buttonRect.bottom}px`;
      interactiveItem.style.left = `${buttonRect.left}px`;

    } else {
      // Muda o símbolo do botão (fecha)
      btn.style.marginBottom = '0px';
      btn.innerText = btn.innerText.replace("▼", "►"); 
    }
  });
}


// Função para gerenciar o pop-up de confirmação
function toggleDeletionPopUp(button) {
  const confirmationPopup = document.getElementById('confirmationPopup');
  const overlay = document.getElementById('overlay');
  const deleteUrl = button.getAttribute('data-url');
  
  // Exibe o pop-up
  confirmationPopup.classList.add('show');
  overlay.classList.add('show');

  // Define a ação de confirmação
  const confirmYes = document.getElementById('confirmYes');
  confirmYes.onclick = () => {
    window.location.href = deleteUrl;
    confirmationPopup.classList.remove('show');
    overlay.classList.remove('show');
  };

  // Cancela o pop-up
  const confirmNo = document.getElementById('confirmNo');
  confirmNo.onclick = () => {
    confirmationPopup.classList.remove('show');
    overlay.classList.remove('show');
  };
}
