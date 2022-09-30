<script lang="ts">
	// @ts-expect-error Import Issue
	import { Field, Input } from 'svelma';
	export let value: string | number | boolean, name: string, editing: boolean;
</script>

<Field>
	<Input {name} {value} disabled={!editing} />
</Field>
