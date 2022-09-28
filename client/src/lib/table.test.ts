import { render, screen, fireEvent } from '@testing-library/svelte';
import Table from './Table.svelte';

describe('Table', () => {
	test('that the tbody is empty', () => {
		render(Table, { props: { products: [] } });
		const tBody = screen.getByRole('table').querySelector('tbody');
		expect(tBody).toBeEmptyDOMElement();
	});
	test('that the tbody has 2 rows', () => {
		render(Table, {
			props: {
				products: [
					{ name: 'foo', price: 1 },
					{ name: 'bar', price: 2 }
				]
			}
		});
		const tBody = screen.getByRole('table').querySelector('tbody');
		expect(tBody).not.toBeEmptyDOMElement();
		expect(tBody?.querySelectorAll('tr')).toHaveLength(2);
	});
});
