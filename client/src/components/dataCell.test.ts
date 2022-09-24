import { render, screen, fireEvent } from '@testing-library/svelte';
import DataCell from './DataCell.svelte';

describe('DataCell', () => {
	test('that the cell is empty', () => {
		render(DataCell, { props: { data: [] } });
		const cell = screen.getByRole('cell');
		expect(cell).not.toBeEmptyDOMElement();
	});
});
