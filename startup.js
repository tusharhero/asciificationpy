function start()
{
    const eqt = document.getElementById('-eqt');
    const size = document.getElementById('-size');
    
    const { searchParams } = new URL(window.location.href);
    
    const inURL =
    {
        eqt: searchParams.get('eqt'),
        size: searchParams.get('size')
    };
        
    if (inURL.eqt !== null && inURL.size !== null)
    {
        eqt.value = inURL.eqt;
        size.value = inURL.size;
    }
};

function submit()
{
    let eqt, size;

    eqt = document.getElementById('text-src').value;
    size = document.getElementById('size').value;

    const param = `?eqt=${eqt}&size=${size}`;

    window.history.replaceState('', '', param);
};

start();

document.getElementById('clear').addEventListener('click', () => window.history.replaceState('', '', '.'));
document.getElementById('submit').addEventListener('click', submit);