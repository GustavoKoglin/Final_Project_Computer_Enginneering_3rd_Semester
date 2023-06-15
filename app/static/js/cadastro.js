function consultarCEP() {
    const cepInput = document.getElementById("cep");
    const cepValue = cepInput.value.replace(/\D/g, ''); // Remove caracteres não numéricos

    if (cepValue.length === 8) {
        fetch(`https://viacep.com.br/ws/${cepValue}/json/`)
            .then(response => response.json())
            .then(data => {
                if (!data.erro) {
                    document.getElementById("logradouro").value = data.logradouro;
                    document.getElementById("bairro").value = data.bairro;
                    document.getElementById("cidade").value = data.localidade;
                    document.getElementById("estado").value = data.uf;
                }
            })
            .catch(error => {
                console.log("Erro ao consultar CEP:", error);
            });
               
        $(document).ready(function() {
            $('#cep').inputmask({
                mask: '**.***.***',
                placeholder: '**.***.***'
            });
        });
        
    }
}
