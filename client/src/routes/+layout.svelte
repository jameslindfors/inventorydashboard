<script>
	import { navigating } from '$app/stores';
</script>

{#if $navigating}
    <div class="loading">Loading...</div>
{/if}

<main>
	<slot />
</main>