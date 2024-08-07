let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
}
// run the anonympus function one all DOM is done loading
document.addEventListener('DOMContentLoaded', function() {
    // the same as <button onclick="count()">
    // document.querySelector('button').addEvenetListener('click', count())
    document.querySelector('button').onclick = count;

    //run the function every second
    setInterval(count, 1000);
})