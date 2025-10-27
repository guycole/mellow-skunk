class CreateProjects < ActiveRecord::Migration[8.0]
  def change
    create_table :projects do |t|
      t.string :name, unique: true
      t.boolean :enable

      t.timestamps
    end
  end
end
