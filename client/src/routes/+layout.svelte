<script>
	import { navigating } from '$app/stores';
</script>

{#if $navigating}
	<div class="loading">Loading...</div>
{/if}

<main class="is-flex is-flex-direction-column mx-4">
	<slot />
</main>
