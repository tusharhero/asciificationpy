function start()
{
    const { searchParams } = new URL(window.location.href);
    
    const inURL =
    {
        eqt: searchParams.get('eqt'),
        size: searchParams.get('size')
    };
        
    if (inURL.eqt !== null && inURL.size !== null)
    {
        document.getElementById('-eqt').value = inURL.eqt;
        document.getElementById('text-src').value = inURL.eqt;

        document.getElementById('-size').value = inURL.size;
        document.getElementById('size').value = inURL.size;
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