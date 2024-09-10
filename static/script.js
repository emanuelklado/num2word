function converterNumero() {
    const numero = document.getElementById('numero').value;
    fetch(`/numero_por_extenso?numero=${numero}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultado').innerText = data.por_extenso;
        })
        .catch(error => {
            console.error('Erro:', error);
            document.getElementById('resultado').innerText = 'Erro ao converter o número';
        });
}
