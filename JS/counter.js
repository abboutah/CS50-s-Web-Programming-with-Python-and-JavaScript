let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;

    if (counter % 10 === 0) {
        // Template literals are delimited by (`)  and a $  and curly braces for var 
        alert(`Count is now ${counter}`);
    }
}
// run the anonympus function one all DOM is done loading
document.addEventListener('DOMContentLoaded', function() {
    // the same as <button onclick="count()">
    // document.querySelector('button').addEvenetListener('click', count())
    document.querySelector('button').onclick = count;
})