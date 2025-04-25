document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('btn-analisar');
  if (!btn) return;

  btn.addEventListener('click', async e => {
    e.preventDefault();
    const pk = btn.dataset.pk;
    const resultEl = document.getElementById('analise-resultado');
    const spinner = document.getElementById('analise-spinner');

    spinner.style.display = 'block';
    btn.disabled = true;

    try {
      const res = await fetch(`/api/politicas/${pk}/analise/`, { method: 'POST' });
      const data = await res.json();
      resultEl.textContent = data.resultado;
    } catch (err) {
      resultEl.textContent = 'Erro ao chamar API.';
    } finally {
      spinner.style.display = 'none';
      btn.disabled = false;
    }
  });
});
