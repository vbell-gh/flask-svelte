<script>
    let rand = -1

    function getRand(){
        fetch('./rand')
            .then(d => t.text())
            .then(d => (rand = d));

    }
</script>

<h1> your number is: {rand}</h1>
<button on:click={getRand}>Get a random number</button>