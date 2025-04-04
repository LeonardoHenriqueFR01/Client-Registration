// Função para trocar de formulários
function toggleForms() {
    document.getElementById('content').classList.toggle('active');
};

// Função para chamar o spin button form de cliente avista
function get_spin_avista() {
    let name = document.getElementById('name_avista').value.trim();
    let name_vehicle = document.getElementById('name_vehicle_avista').value.trim();
    let value_vehicle = document.getElementById('value_vehicle_avista').value.trim();
    let value_prohibited = document.getElementById('value_prohibited_avista').value.trim();

    let btn_avista = document.getElementById('btn_avista');
    let load_avista = document.getElementById('load_avista');

    if (name.length < 3) {
        alert('O nome do cliente deve ter no mínimo 3 caracteres!');
        return;
    }

    if (name_vehicle.length < 3) {
        alert('O nome do veiculo deve ter no mínimo 3 caracteres!');
        return;
    }

    if (value_vehicle.length < 3) {
        alert('O valor do veiculo deve ter no mínimo 3 caracteres!');
        return;
    }

    if (value_prohibited.length < 3) {
        alert('O valor de entrada deve ter no mínimo 3 caracteres!');
        return;
    }

    // Caso nenhuma das opções a cima aconteça
    btn_avista.style.display = 'none';
    load_avista.style.display = 'block';

};

// Função para chamar o spin button form de cliente financiamento
function get_spin_financia() {
    let name = document.getElementById('name').value.trim();
    let name_vehicle = document.getElementById('name_vehicle').value.trim();
    let value_vehicle = document.getElementById('value_vehicle').value.trim();
    let value_prohibited = document.getElementById('value_prohibited').value.trim();

    let btn_financia = document.getElementById('btn_financia');
    let load_financia = document.getElementById('load_financia');

    if (name.length < 3) {
        alert('O nome do cliente deve ter no mínimo 3 caracteres!');
        return;
    }

    if (name_vehicle.length < 3) {
        alert('O nome do veiculo deve ter no mínimo 3 caracteres!');
        return;
    }

    if (value_vehicle.length < 3) {
        alert('O valor do veiculo deve ter no mínimo 3 caracteres!');
        return;
    }

    if (value_prohibited.length < 3) {
        alert('O valor de entrada deve ter no mínimo 3 caracteres!');
        return;
    }

    // Caso nenhuma das opções a cima aconteça
    btn_financia.style.display = 'none';
    load_financia.style.display = 'block';
    
};