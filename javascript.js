function start()
{
    const { searchParams } = new URL(window.location.href);
    
    const display = searchParams.get('display');

    if (display === null) return;

    const [eqt, size, scale] = atob(display).split('/|');

    document.getElementById('-eqt').value = eqt;
    document.getElementById('text-src').value = eqt;

    document.getElementById('-size').value = size;
    document.getElementById('size').value = size;

    document.getElementById('-scale').value = scale;
    document.getElementById('scaling').value = scale;
};

function submit()
{
    const eqt = document.getElementById('text-src').value;
    const size = document.getElementById('size').value;
    const scale = document.getElementById('scaling').value;

    window.history.replaceState('', '', `?display=${btoa(`${eqt}/|${size}/|${scale}`)}`);
};

function share()
{
    navigator.clipboard.writeText(document.URL)
    .then(() => document.getElementById('error').innerText = '$ Link copied to clipboard!');    
};

start();

document.getElementById('clear').addEventListener('click', () => window.history.replaceState('', '', '.'));
document.getElementById('submit').addEventListener('click', submit);
document.getElementById('share').addEventListener('click', share);