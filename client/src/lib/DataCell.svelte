<script lang="ts">
	import { Field, Input } from 'svelma';
	export let cellData, status;
</script>

<td>
	<Field>
		<Input type="text" value={cellData} disabled={status} />
	</Field>
</td>
