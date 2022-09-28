<script type="ts">
	import 'bulma/css/bulma.css';
	import { Tabs, Tab } from 'svelma';
	import Nav from '$lib/Nav.svelte';
	import Table from '$lib/Table.svelte';

	type CollectionData = {
		data: [
			{
				id: number;
				name: string;
				description: string;
				products: [any];
			}
		];
	};

	export let data: CollectionData;

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
