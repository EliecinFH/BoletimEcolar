console.log("Script carregado");

// Função para exibir a aba correspondente ao resultado
function showTab(tabId) {
    // Oculta todas as abas
    var tabs = document.getElementsByClassName('tab-content');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].style.display = 'none';

    }
    // Exibe a aba correspondente ao ID passado como argumento
    document.getElementById(tabId).style.display = 'block';
    
}