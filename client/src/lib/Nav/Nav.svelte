<script lang="ts">
	// @ts-expect-error Import Issue
	import { Button } from 'svelma';
	import NewCollectionModel from '../NewCollectionModal/NewCollectionModal.svelte';

	let active = false;
</script>

<nav class="is-flex is-full is-justify-content-space-between is-align-items-center">
	<h1 class="is-size-2">Inventory Manager</h1>
	<div
		class="is-flex is-flex-direction-row flex-1 is-justify-content-space-between is-align-items-center"
	>
		<div class="is-flex is-flex-direction-row is-justify-content-space-between mt-2">
			<span class="mx-2">
				<Button on:click={() => (active = !active)} type="is-info">New Collection</Button>
				<NewCollectionModel {active} />
			</span>
			<a href="/analytics">
				<Button type="is-dark">Analytics</Button>
			</a>
		</div>
	</div>
</nav>
