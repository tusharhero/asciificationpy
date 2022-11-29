const SIZELIMIT = parseInt(document.getElementById('-sizeLimit').innerHTML);

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

function sizeLimit()
{
    const size = parseInt(document.getElementById('size').value);

    if (size < SIZELIMIT) return false;

    document.getElementById('modalWrapper').style.display = 'flex';

    return true;
};

function submit()
{
    const eqt = document.getElementById('text-src').value;
    const size = document.getElementById('size').value;
    const scale = document.getElementById('scaling').value;

    sizeLimit() ? null : window.history.replaceState('', '', `?display=${btoa(`${eqt}/|${size}/|${scale}`)}`);
};

function share()
{
    navigator.clipboard.writeText(window.location.href)
    .then(() => document.getElementById('error').innerText = '$ Link copied to clipboard!');    
};

start();

document.getElementById('clear').addEventListener('click', () => window.history.replaceState('', '', '.'));
document.getElementById('submit').addEventListener('click', submit);
document.getElementById('share').addEventListener('click', share);
document.getElementById('modalClose').addEventListener('click', () => document.getElementById('modalWrapper').style.display = 'none');

['text-src', 'size', 'scaling'].forEach(x => document.getElementById(x).addEventListener('keydown', (E) => E.key === 'Enter' ? sizeLimit() : null));