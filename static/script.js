let editModeId = null;

// Function to fetch commands from our Python API
async function loadCommands() {
    const response = await fetch('/api/commands');
    const commands = await response.json();
    
    const tableBody = document.getElementById('commandTable');
    tableBody.innerHTML = ''; // Clear current table
    
    commands.forEach(c => {
    const row = `<tr>
    <td><code>${c.cmd}</code></td>
    <td>${c.description}</td>
    <td class="text-end">
        <button onclick="prepareEdit(${c.id}, '${c.cmd}', '${c.description}')" class="btn btn-sm btn-warning">Edit</button>
        <button onclick="deleteCommand(${c.id})" class="btn btn-sm btn-danger">Delete</button>
    </td>
                </tr>`;
    tableBody.insertAdjacentHTML('beforeend', row);
});
   

}

async function addCommand() {
    const cmd = document.getElementById('cmdInput').value;
    const description = document.getElementById('descInput').value;

    if (editModeId) {
        // Tady posíláme PUT na /api/commands/ID
        console.log("Updating command with ID:", editModeId); // Ladicí výpis
        await fetch(`/api/commands/${editModeId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cmd, description })
        });
        editModeId = null; // Důležité: vypnout editaci
        document.querySelector('button[onclick="addCommand()"]').innerText = "Save";
    } else {
        // Klasický POST
        await fetch('/api/commands', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cmd, description })
        });
    }
    // Vyčistíme políčka a načteme tabulku
    document.getElementById('cmdInput').value = '';
    document.getElementById('descInput').value = '';
    loadCommands();
}

//  Function to delete a command by ID
async function deleteCommand(id) {
    if (!confirm('Are you sure you want to delete this command?')) return;

    await fetch(`/api/commands/${id}`, {
        method: 'DELETE'
    });

    loadCommands(); // Znovu načteme tabulku, aby zmizel smazaný řádek
}

function prepareEdit(id, cmd, description) {
    // 1. Vyplníme políčka daty z řádku, na který jsme klikli
    document.getElementById('cmdInput').value = cmd;
    document.getElementById('descInput').value = description;
    
    // 2. Přepneme se do editovacího módu (uložíme si ID)
    editModeId = id;
    
    // 3. Změníme text tlačítka, aby uživatel věděl, že edituje
    document.querySelector('button[onclick="addCommand()"]').innerText = "Update";
}
// Initial load when page opens
loadCommands();