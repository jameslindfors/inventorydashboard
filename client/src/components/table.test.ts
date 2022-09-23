import { render, screen, fireEvent } from '@testing-library/svelte'
import Table from './Table.svelte'

describe('Table', () => {
    test("that the tbody is empty", () => {
        render(Table, { props: { products:  [] }});
        const tBody = screen.getByRole('table').querySelector('tbody');
        expect(tBody).toBeEmptyDOMElement();
    })
})