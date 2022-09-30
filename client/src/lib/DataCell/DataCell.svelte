<script lang="ts">
	// @ts-expect-error
	import { Field, Input } from 'svelma';

	export let cellData: string | number | boolean, status: boolean, formId: string, cellType: string;

</script>

<td id={cellType}>
		<Field>
			<Input type="text" form={formId} value={cellData} disabled={status} />
		</Field>
</td>
