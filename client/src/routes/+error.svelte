<script context="module">
	import { page } from '$app/stores';
</script>

<svelte:head>
	<title>{$page.status}</title>
</svelte:head>

<div class="col-md-9">
	<h1>{$page.status}</h1>

	<p>{$page?.error?.message}</p>
</div>
