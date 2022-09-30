<script type="ts">
	import 'bulma/css/bulma.css';
	import type { CollectionType } from '../types/collection.type';
	// @ts-expect-error
	import { Tabs, Tab } from 'svelma';
	import Nav from '$lib/Nav/Nav.svelte';
	import Table from '$lib/Table/Table.svelte';

	export let data: CollectionType;

	const tabs = data.data
		.map((collection) => {
			return {
				label: collection.name,
				component: Table,
				props: {
					products: collection.products
				}
			};
		})
		.slice(0, 5);
</script>

<svelte:head>
	<title>Dashboard</title>
</svelte:head>
<Nav />
<br />
<Tabs style="is-boxed">
	{#each tabs as tab}
		<Tab label={tab.label}>
			{#if tab.component}
				<svelte:component this={tab.component} {...tab.props} />
			{/if}
		</Tab>
	{/each}
</Tabs>
