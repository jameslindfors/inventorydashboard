<script lang="ts">
	// @ts-expect-error Import Issue
	import { Modal } from 'svelma';
	export let active: boolean;
</script>

<Modal bind:active>
	<section class="has-background-light">
		<h1 class="title">New Collection</h1>
	</section>
</Modal>
