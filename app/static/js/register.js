// Função para trocar de formulário
function toggleForms() {
    document.getElementById('content').classList.toggle('active');
};

// Função para chamar o spin button form de cadastro
function get_spin_cadastro() {
    let name = document.getElementById('name').value.trim();
    let email = document.getElementById('email').value.trim();
    let password = document.getElementById('password').value.trim();

    let btn_cadastro = document.getElementById('btn_cadastro');
    let load_cadastro = document.getElementById('load_cadastro');

    if (name.length < 3) {
        alert('O nome deve ter no mínimo 3 caracteres!');
        return;
    };

    if (email.length < 12) {
        alert('O email deve ter no mínimo 12 caracteres!')
        return;
    };

    if (password.length < 8) {
        alert('A senha deve ter no mínimo 8 caracteres!');
        return;
    };

    // Caso nehuma das opções a cima aconteça
    btn_cadastro.style.display = 'none'
    load_cadastro.style.display = 'block'

};

// Função para chamar o spin button form de login
function get_spin_login() {
    let name = document.getElementById('name_login').value.trim();
    let email = document.getElementById('email_login').value.trim();
    let password = document.getElementById('password_login').value.trim();

    let btn_login = document.getElementById('btn_login');
    let load_login = document.getElementById('load_login');

    if (name.length < 3) {
        alert('O nome deve ter no mínimo 3 caracteres!');
        return;
    };

    if (email.length < 12) {
        alert('O email deve ter no mínimo 12 caracteres!')
        return;
    };

    if (password.length < 8) {
        alert('A senha deve ter no mínimo 8 caracteres!');
        return;
    };

    // Caso nehuma das opções a cima aconteça
    btn_login.style.display = 'none'
    load_login.style.display = 'block'

};
