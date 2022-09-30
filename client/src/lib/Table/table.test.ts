import { render, screen } from '@testing-library/svelte';
import Table from './Table.svelte';

describe('Table', () => {
	test('that the table is rendered', () => {
		render(Table);
		const table = screen.getByRole('table');
		expect(table).toBeInTheDocument();
	});
});
